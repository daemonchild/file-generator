# Build Script for File Generator
# Paste into your Launch Template
apt-get update
apt-get install -y docker.io
git clone https://github.com/daemonchild/file-generator.git
cd file-generator
docker build -t file-gen:latest .
docker run -d -p 80:9000 --name file-gen-app file-gen:latest
docker update --restart always file-gen-app