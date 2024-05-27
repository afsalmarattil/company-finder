export class ApiService {
    baseUrl: string;

    constructor(baseUrl: string) {
        this.baseUrl = baseUrl;
    }

    async fetchFromApi<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
        try {
            const response = await fetch(`${this.baseUrl}${endpoint}`, options);
            if (!response.ok) {
                throw new Error(`Network response was not ok: ${response.statusText}`);
            }
            return await response.json() as T;
        } catch (error) {
            console.error("API error:", error);
            throw error;
        }
    }
}


const apiService = new ApiService(import.meta.env.VITE_API_URL);
export default apiService;
