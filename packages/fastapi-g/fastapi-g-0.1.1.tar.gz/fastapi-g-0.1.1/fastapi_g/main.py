import os
import json
import argparse
from tqdm import tqdm
import sys
import subprocess

def generate_project_structure(input_file, project_name):
    with open(input_file, 'r') as f:
        data = json.load(f)

    total_models = len(data)
    # total_processes = total_models * 7
    total_processes = 7
    current_process = 0
    for model_name, fields in tqdm(data.items(), desc="Generating project structure", total=total_processes):
        # Create model file
        generate_model_file(model_name, fields, project_name)
        current_process += 1

        # Create DTO file
        generate_dto_file(model_name, fields, project_name)
        current_process += 1

        # Create service file
        generate_service_file(model_name, fields, project_name)
        current_process += 1

        # Create repository file
        generate_repository_file(model_name, project_name)
        current_process += 1

        # Create router file
        generate_router_file(model_name, project_name)
        current_process += 1

        # Create user file
        generate_user_files(model_name, project_name)
        current_process += 1

        # Create util file
        generate_util_files(project_name)
        current_process += 1

        progress_percent = current_process / total_processes * 100
        tqdm.write(f"Progress: {progress_percent:.2f}%")

def generate_model_file(model_name, fields, project_name):
    model_folder = os.path.join(project_name, 'model', model_name)
    os.makedirs(model_folder, exist_ok=True)
    model_file = os.path.join(model_folder, f'{model_name}.py')

    with open(model_file, 'w') as mf:
        mf.write(f'from pydantic import BaseModel\n\n')
        mf.write(f'class {model_name}(BaseModel):\n')
        for field, data_type in fields.items():
            mf.write(f'    {field}: {map_data_type(data_type)}\n')

def generate_dto_file(model_name, fields, project_name):
    dto_folder = os.path.join(project_name, 'dto')
    os.makedirs(dto_folder, exist_ok=True)
    dto_file = os.path.join(dto_folder, f'{model_name.lower()}_dto.py')

    with open(dto_file, 'w') as df:
        df.write(f'class {model_name}DTO:\n')
        for field, data_type in fields.items():
            df.write(f'    {field}: {map_data_type(data_type)}\n')

def generate_service_file(model_name, fields, project_name):
    service_folder = os.path.join(project_name, 'service')
    os.makedirs(service_folder, exist_ok=True)
    service_file = os.path.join(service_folder, f'{model_name.lower()}_service.py')

    with open(service_file, 'w') as sf:
        sf.write(f'class {model_name}Service:\n')
        sf.write(f'    def __init__(self):\n')
        sf.write(f'        self.data = []\n\n')

        # Generate get method
        sf.write(f'    def get_{model_name.lower()}(self, {model_name.lower()}_id: int):\n')
        sf.write(f'        for item in self.data:\n')
        sf.write(f'            if item["{model_name.lower()}_id"] == {model_name.lower()}_id:\n')
        sf.write(f'                return item\n')
        sf.write(f'        return None\n\n')

        # Generate put method
        sf.write(f'    def put_{model_name.lower()}(self, {model_name.lower()}_id: int, {model_name.lower()}_data: dict):\n')
        sf.write(f'        for index, item in enumerate(self.data):\n')
        sf.write(f'            if item["{model_name.lower()}_id"] == {model_name.lower()}_id:\n')
        sf.write(f'                self.data[index] = {model_name.lower()}_data\n')
        sf.write(f'                return True\n')
        sf.write(f'        return False\n\n')

        # Generate post method
        sf.write(f'    def post_{model_name.lower()}(self, {model_name.lower()}_data: dict):\n')
        sf.write(f'        self.data.append({model_name.lower()}_data)\n')
        sf.write(f'        return {model_name.lower()}_data\n')

def generate_repository_file(model_name, project_name):
    repository_folder = os.path.join(project_name, 'repository')
    os.makedirs(repository_folder, exist_ok=True)
    repository_file = os.path.join(repository_folder, f'{model_name.lower()}_repository.py')

    with open(repository_file, 'w') as rf:
        rf.write(f'class {model_name}Repository:\n')
        rf.write(f'    pass\n')

def generate_router_file(model_name, project_name):
    router_folder = os.path.join(project_name, 'router')
    os.makedirs(router_folder, exist_ok=True)
    router_file = os.path.join(router_folder, f'{model_name.lower()}_router.py')

    with open(router_file, 'w') as rf:
        rf.write(f'from fastapi import APIRouter\n')
        rf.write(f'from service.{model_name.lower()}_service import {model_name}Service\n\n')
        rf.write(f'router = APIRouter()\n')
        rf.write(f'service = {model_name}Service()\n\n')
        rf.write(f'# Define endpoints for {model_name} CRUD operations\n')
        rf.write(f'# Example:\n')
        rf.write(f'@router.get("/{model_name.lower()}s/{{{model_name.lower()}_id}}")\n')
        rf.write(f'async def get_{model_name.lower()}({model_name.lower()}_id: int):\n')
        rf.write(f'    return service.get_{model_name.lower()}({model_name.lower()}_id)\n')

def map_data_type(data_type):
    data_type_mapping = {
        'str': 'str',
        'int': 'int',
        'blob': 'bytes',
        'datetime': 'str'}
    return data_type_mapping.get(data_type, 'str')

def generate_user_files(model_name, project_name):
    user_folder = os.path.join(project_name, 'user')
    os.makedirs(user_folder, exist_ok=True)
    user_service_file = os.path.join(user_folder, f'user_service.py')
    user_repository_file = os.path.join(user_folder, f'user_repository.py')
    user_router_file = os.path.join(user_folder, f'user_router.py')
    # Generate other files as needed for user management
    with open(user_service_file, 'w') as usf:
        usf.write('# Your user service implementation goes here\n')
    with open(user_repository_file, 'w') as urf:
        urf.write('# Your user repository implementation goes here\n')
    with open(user_router_file, 'w') as urf:
        urf.write('# Your user router implementation goes here\n')

def generate_util_files(project_name):
    util_folder = os.path.join(project_name, 'util')
    os.makedirs(util_folder, exist_ok=True)
    hash_file = os.path.join(util_folder, f'hash_util.py')
    jwt_file = os.path.join(util_folder, f'jwt_util.py')
    # Generate other util files as needed
    with open(hash_file, 'w') as hf:
        hf.write('# Your hash utility implementation goes here\n')
    with open(jwt_file, 'w') as jf:
        jf.write('# Your JWT utility implementation goes here\n')

def generate_main_file(project_name, input):
    router_names = get_router_names(input)
    main_file_path = os.path.join(project_name, 'main.py')
    with open(main_file_path, 'w') as file:
        file.write("import uvicorn\n")
        file.write("from fastapi import FastAPI\n")

        for router_name in router_names:
            file.write(f"from router.{router_name} import router as {router_name}\n")
        file.write("\n")

        file.write("app = FastAPI()\n\n")

        for router_name in router_names:
            file.write(f"app.include_router({router_name})\n")
        file.write("\n")

        file.write("if __name__ == '__main__':\n")
        file.write("    uvicorn.run(app, host='0.0.0.0', port=8000)\n")

def install_dependencies(project_name):
    requirements_path = os.path.join(project_name, 'requirements.txt')
    print(f"Generating {requirements_path}...")
    with open(requirements_path, 'w') as file:
        file.write('pydantic\nfastapi\nuvicorn\n')
    print("Installing dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_path])

def get_router_names(input_file):
    router_names = []
    with open(input_file, 'r') as f:
        data = json.load(f)

        for model_name, fields in tqdm(data.items(), desc="Generating project structure"):
            router_names.append(f'{model_name.lower()}_router')
        return router_names

def main():
    parser = argparse.ArgumentParser(description='Generate FastAPI project structure from JSON')
    parser.add_argument('--input', type=str, help='Path to JSON input file', required=True)
    parser.add_argument('--project_name', type=str, help='Name of the project', required=True)

    try:
        args = parser.parse_args()

        # Create project folder
        project_name = args.project_name
        os.makedirs(project_name, exist_ok=True)

        # Install dependencies if not installed
        install_dependencies(project_name)

        # Generate main.py
        generate_main_file(project_name, args.input)

        # Continue with generating file process
        generate_project_structure(args.input, args.project_name)

        print('Project structure generated successfully.')
    except argparse.ArgumentError as e:
        print(f"Error: {str(e)}")
        print("Usage:")
        parser.print_usage()
        sys.exit(1)

if __name__ == '__main__':
    main()