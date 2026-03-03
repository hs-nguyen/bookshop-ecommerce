#!/bin/bash

# Frontend Setup Script for Bookshop E-commerce

echo "Setting up frontend project..."

# Create frontend with Vite
npm create vite@latest frontend -- --template vue

cd frontend

# Install dependencies
echo "Installing dependencies..."
npm install
npm install vue-router pinia axios

# Create directory structure
echo "Creating directory structure..."
mkdir -p src/api
mkdir -p src/components
mkdir -p src/views
mkdir -p src/store
mkdir -p src/router

echo "Frontend setup complete!"
echo "Next steps:"
echo "1. cd frontend"
echo "2. npm run dev"
echo "3. Start implementing components"
