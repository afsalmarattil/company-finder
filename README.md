Company Finder
Company Finder is a powerful tool designed to streamline the process of searching for companies and identifying similar entities in the industry. 

Company Search: A search bar to find companies by name.
Company Profile: A display area showing detailed information about a selected company, containing a button that finds similar companies.
Similar Companies: A separate section to display a list of N companies that are similar to a chosen company.

features:
1) Settings page to upload company data. Data should be in cs format and should contain the below columns
   id,linkedin_url,company_name,industry,website,tagline,about,year_founded,locality,country,current_employee_estimate,keywords
2) companies page that displays all companies
3) Search by company name
4) Company detail page
5) Similar companies - keyword and industry-based search


Technology stack:
1) API - http://localhost:8000/docs (fastapi)
2) Data storage and indexing - Elastic search
3) Front end - sveletekit


To Run:
1) create a folder "esdata" at root
2) docker-compose up
3) go to http://localhost:8080/


@todo
1) Modify the existing API to support both keyword and semantic searches
2) Add Question Answering for comapny data
