#!/bin/bash

# project configuration script

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

usage() {
    echo "Usage: $0 --name <project_name> --description <project_description>"
    exit 1
}

escape_sed_replacement() {
    printf '%s' "$1" | sed -e 's/[&|]/\\&/g'
}

if [ "$#" -lt 4 ]; then
    usage
fi

while [ "$#" -gt 0 ]; do
    case "$1" in
        --name)
            project_name="$2"
            shift 2
            ;;
        --description)
            project_description="$2"
            shift 2
            ;;
        *)
            usage
            ;;
    esac
done

if [ -z "$project_name" ] || [ -z "$project_description" ]; then
    usage
fi

# turn the project name - into _ for pythons sake
project_name_underscore=$(echo "$project_name" | sed 's/-/_/g')
project_name_escaped=$(escape_sed_replacement "$project_name")
project_name_underscore_escaped=$(escape_sed_replacement "$project_name_underscore")
project_description_escaped=$(escape_sed_replacement "$project_description")

# 1. rename the module and actions folders
if [ -d "module" ]; then
    mv module "${project_name_underscore}"
fi

if [ -d ".github_template" ]; then
    mv .github_template .github
fi

# 2. Define the files to be modified
files_to_replace=(
    "Makefile"
    "pyproject.toml"
)

# 3. Replace the placeholders in each file
for file in "${files_to_replace[@]}"; do
    if [ -f "$file" ]; then
        sed -i "s|<name-placeholder>|$project_name_escaped|g" "$file"
        sed -i "s|<name-placeholder-underscore>|$project_name_underscore_escaped|g" "$file"
        sed -i "s|<description-placeholder>|$project_description_escaped|g" "$file"
    fi
done

# 4. Generate uv lockfile when uv is available
if command -v uv >/dev/null 2>&1; then
    uv lock
else
    echo "uv not found, skipping lockfile generation. Run 'uv lock' manually after installing uv."
fi

# 5. Remove the instructions_file and configure.sh
rm -f instructions_after_clone.txt
rm -f configure.sh
