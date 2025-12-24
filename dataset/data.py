import kagglehub

# Download latest version
path = kagglehub.dataset_download("suraj520/indian-household-electricity-bill")

print("Path to dataset files:", path)