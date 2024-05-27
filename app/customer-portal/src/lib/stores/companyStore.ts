import {  writable, get, type Writable, derived } from 'svelte/store';
import type { Company, Pagination } from '../types/company';
import apiService from '$lib/api';
import { browser } from '$app/environment';

export const companies: Writable<Company[]> = writable([]);
export const currentCompany: Writable<Company | null> = writable(null);
export const similarCompanies: Writable<Company[]> = writable([]);
export const paginationInfo: Writable<Pagination | null> = writable(null);

export const searchQuery: Writable<string> = writable("");
export const isSearching = derived(searchQuery, $searchQuery => $searchQuery.trim() !== "");

export  const fetchCompanies= async(page: number = 1, page_size: number = 12, append: boolean = false): Promise<void> => {
    if (!browser || get(isSearching)) return;

  console.log("fetchCompanies called")

  try {
      const response = await apiService.fetchFromApi<{results: Company[], pagination: Pagination}>(
          `/companies?page=${page}&page_size=${page_size}`
      );

      if (append) {
        companies.update((existingCompanies) => [...existingCompanies, ...response.results]);
    } else {
        companies.set(response.results);
    }

      paginationInfo.set({
          total: response.total,
          page: response.page,
          page_size: response.page_size,
          total_pages: response.total_pages
      });
  } catch (error) {
      console.error("Failed to fetch companies:", error);
      companies.set([]);
      paginationInfo.set(null);
  }
}

export const loadNextPage = (): void=> {
    const pagination = get(paginationInfo);
    if (pagination && pagination.page < pagination.total_pages) {
        const nextPage = pagination.page + 1;
        fetchCompanies(nextPage, pagination.page_size, true);
    }
}


export  const fetchCompany = async (companyId: string): Promise<void> =>{
    if (!browser) return; 
    try {
        const company: Company = await apiService.fetchFromApi<Company>(`/companies/${companyId}`);
        currentCompany.set(company);
    } catch (error) {
        console.error("Failed to fetch company:", error);
        currentCompany.set(null);
    }
}

export const searchCompanies = async (query: string): Promise<void> =>{
    if (!browser) return;
    try {
        companies.set([]); 
        const results: Company[] = await apiService.fetchFromApi<Company[]>(`/companies/search/${encodeURIComponent(query)}`);
        console.log(results)
        companies.set(results);
    } catch (error) {
        console.error("Failed to search companies:", error);
        companies.set([]);
    }
}

export const fetchSimilarCompanies = async(companyId: string): Promise<void> =>{
    if (!browser) return; 

    try {
        const data: Company[] = await apiService.fetchFromApi<Company[]>(`/companies/similar/${companyId}`);
        similarCompanies.set(data);
    } catch (error) {
        console.error("Failed to fetch similar companies:", error);
        similarCompanies.set([]);
    }
}

export const uploadCSV= async(file: File) =>{
    const formData = new FormData();
    formData.append('file', file);
    
    return apiService.fetchFromApi('/data/upload-csv/', {
      method: 'POST',
      body: formData
    });
  }