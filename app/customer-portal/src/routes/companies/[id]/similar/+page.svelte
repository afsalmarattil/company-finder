<script lang="ts">
  import { onMount } from "svelte";
  import { page } from "$app/stores";
  import {
    fetchCompany,
    fetchSimilarCompanies,
    currentCompany,
    similarCompanies,
  } from "$lib/stores/companyStore";
  import CompanyCard from "$lib/components/cards/CompanyCard.svelte";
  import { Breadcrumb, BreadcrumbItem } from "flowbite-svelte";
  import NoData from "$lib/components/error/NoData.svelte";

  let companyId: string;
  $: companyId = $page.params.id;

  onMount(async () => {
    if (companyId) {
      await fetchCompany(companyId);
      await fetchSimilarCompanies(companyId);
    }
  });
</script>

<div class="flex p-4 justify-between align-middle">
  <h1 class="text-xl dark:text-white">
    <span class="text-sm">Companies similar to</span>
    {$currentCompany?.company_name || ""}
  </h1>
  <Breadcrumb aria-label="Default breadcrumb example">
    <BreadcrumbItem href="/companies" home>Companies</BreadcrumbItem>
    <BreadcrumbItem href={`/companies/${$currentCompany?.id}`}
      >{$currentCompany?.company_name || "Loading..."}</BreadcrumbItem
    >
    <BreadcrumbItem>similar</BreadcrumbItem>
  </Breadcrumb>
</div>

{#if !$similarCompanies.length}
  <NoData message="No similar company data found" />
{/if}

<section class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4 p-4">
  {#each $similarCompanies as company (company.id)}
    <CompanyCard {company} />
  {/each}
</section>
