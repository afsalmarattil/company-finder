<script lang="ts">
  import { page } from "$app/stores";
  import {
    fetchCompany,
    fetchSimilarCompanies,
    currentCompany,
    similarCompanies,
  } from "$lib/stores/companyStore";
  import RecommendationCard from "$lib/components/cards/RecommendationCard.svelte";
  import { Avatar, Breadcrumb, BreadcrumbItem } from "flowbite-svelte";
  import {
    ClockOutline,
    LinkOutline,
    LinkedinSolid,
    MapPinAltOutline,
    StoreOutline,
    UserCircleOutline,
  } from "flowbite-svelte-icons";
  import InfoItem from "$lib/components/Info/InfoItem.svelte";
  import NoData from "$lib/components/error/NoData.svelte";

  $: companyId = $page.params.id;

  $: {
    if (companyId) {
      fetchCompanyData(companyId);
    }
  }

  const fetchCompanyData = async (companyId: string) => {
    await fetchCompany(companyId);
    await fetchSimilarCompanies(companyId);
  };
</script>

<div class="flex p-4 justify-end align-middle">
  <Breadcrumb aria-label="Default breadcrumb example">
    <BreadcrumbItem href="/companies" home>Companies</BreadcrumbItem>
    <BreadcrumbItem href={`/companies/${$currentCompany?.id}`}
      >{$currentCompany?.company_name || "Loading..."}</BreadcrumbItem
    >
  </Breadcrumb>
</div>

{#if $currentCompany}
  <div class="flex w-full justify-between space-x-11">
    <div class="w-9/12 px-2">
      <div class="flex items-start space-x-4 rtl:space-x-reverse">
        <Avatar
          size="lg"
          src="/company-placeholder.png"
          alt="comany-logo"
          border
          class="flex-shrink-0 ring-red-400 dark:ring-red-300"
        />
        <div class="flex flex-col space-y-2">
          <p
            class="text-2xl font-medium text-gray-900 truncate dark:text-white"
          >
            {$currentCompany?.company_name ?? ""}
          </p>

          <div class="flex items-center space-x-2">
            <StoreOutline class="text-gray-500 h-5 w-5" />

            <p class="text-sm text-gray-700 truncate dark:text-gray-400">
              {$currentCompany?.industry ?? ""}
            </p>
          </div>
          <div class="flex items-center space-x-2">
            <LinkOutline class="text-gray-500 h-5 w-5" />
            <a
              href={$currentCompany?.website ?? ""}
              target="_blank"
              class="text-sm text-gray-500 truncate dark:text-gray-400"
            >
              {$currentCompany?.website ?? ""}
            </a>
            <a
              href={`https://${$currentCompany?.linkedin_url}`}
              target="_blank"
              class="text-sm text-gray-500 truncate dark:text-gray-400"
            >
              <LinkedinSolid class="text-gray-500 h-5 w-5" />
            </a>
          </div>
        </div>
      </div>

      <div class="flex justify-between py-8">
        <InfoItem
          icon={MapPinAltOutline}
          title="Country"
          value={$currentCompany?.country || "N/A"}
        />
        <InfoItem
          icon={MapPinAltOutline}
          title="Locality"
          value={$currentCompany?.locality || "N/A"}
        />
        <InfoItem
          icon={ClockOutline}
          title="Founded Year"
          value={$currentCompany?.year_founded?.toString() || "N/A"}
        />
        <InfoItem
          icon={UserCircleOutline}
          title="Employees"
          value={$currentCompany?.current_employee_estimate?.toString() ||
            "N/A"}
        />
      </div>

      <div
        class="w-full px-8 py-8 bg-white dark:bg-gray-800 text-gray-900 dark:text-white shadow-sm rounded-lg"
      >
        <h4 class="text-lg font-semibold mb-4 dark:text-gray-400">
          About {$currentCompany?.company_name ?? ""}
        </h4>
        <p class="text-lg italic py-2 text-gray-800 dark:text-gray-200">
          "{$currentCompany?.tagline ?? ""}"
        </p>

        <p class="text-md text-gray-700 dark:text-gray-200">
          {$currentCompany?.about ?? ""}
        </p>
      </div>
    </div>

    <div class="min-w-80 w-full md:w-3/12">
      <section>
        <p class="text-sm mt-2 py-2 text-gray-500">Similar companies</p>
        {#each $similarCompanies as company (company.id)}
          <div class="py-1 w-full">
            <RecommendationCard {company} class="w-full" />
          </div>
        {/each}
      </section>
    </div>
  </div>
{:else}
  <NoData message="No company data found" />
{/if}
