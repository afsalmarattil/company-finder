import { writable, derived } from 'svelte/store';

const activeLoads = writable(new Set());

export const isLoading = derived(activeLoads, ($activeLoads) => $activeLoads.size > 0);

export function startLoading(id:string) {
  activeLoads.update((loads) => {
    loads.add(id);
    return loads;
  });
}

export function stopLoading(id:string) {
  activeLoads.update((loads) => {
    loads.delete(id);
    return loads;
  });
}
