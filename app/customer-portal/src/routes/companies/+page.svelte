<script lang="ts">
  import CompanyCard from "$lib/components/cards/CompanyCard.svelte";
  import {
    companies,
    fetchCompanies,
    loadNextPage,
    searchQuery,
  } from "$lib/stores/companyStore";
  import { Badge } from "flowbite-svelte";
  import { onMount } from "svelte";
  import { intersectionObserver } from "$lib/utils/intersectionObserver";
  import NoData from "$lib/components/error/NoData.svelte";

  onMount(() => {
    if ($searchQuery.trim() === "") {
      fetchCompanies();
    }
  });
</script>

<svelte:head>
  <title>Company Finder</title>
  <meta
    name="description"
    content="Find and explore companies from all around the world."
  />
</svelte:head>

{#if !$companies.length}
  <NoData message="No company data found" />
{/if}
<section class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4 p-4">
  {#each $companies as company (company.id)}
    <CompanyCard {company} />
  {/each}
</section>

<div use:intersectionObserver={loadNextPage} class="h-1"></div>
