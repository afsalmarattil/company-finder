export interface Company {
    id: number;
    linkedin_url: string;
    company_name: string;
    industry: string;
    website: string;
    tagline: string | null;
    about: string;
    year_founded: number;
    locality: string;
    country: string;
    current_employee_estimate: number;
    keywords: string;
}

export interface RouteParams {
    id: string;
}

export interface Pagination {
    total: number;
    page: number;
    page_size: number;
    total_pages: number;
}