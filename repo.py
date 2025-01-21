from huggingface_hub import HfApi

hf_token = ""
repo_name = ""  # Name of your new repo
repo_type = ""  # Choose from: 'model', 'dataset', 'space'
private = True  # Set to True if you want the repo to be private

# Initialize API
api = HfApi()

# Create repository
repo_url = api.create_repo(
    repo_id=repo_name,  # Use repo_id instead of name
    token=hf_token,
    repo_type=repo_type,
    private=private,
)

print(f"Repository created successfully: {repo_url}")
