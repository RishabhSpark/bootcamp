with open("insert_companies.sql", "w") as f:
    for i in range(2, 501):
        company_name = f"Company{i}"
        f.write(f"INSERT INTO COMPANIES (company_name, id) VALUES ('{company_name}', {i});\n")