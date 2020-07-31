source .env

# Create secondary Database
echo "CREATE DATABASE hr_db" |\
    psql $(echo $DATABASE_URL |\
    cut -d '/' -f 1-3 | xargs -I "%" echo %/)
