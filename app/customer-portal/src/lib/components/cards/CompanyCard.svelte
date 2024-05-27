<script lang="ts">
  import type { Company } from "$lib/types/company";
  import { Card, Avatar, Button } from "flowbite-svelte";
  import { goto } from "$app/navigation";

  export let company: Company;

  function viewDetail() {
    goto(`/companies/${company.id}`);
  }

  function viewSimilar() {
    goto(`/companies/${company.id}/similar`);
  }
</script>

<Card padding="md">
  <div class="flex flex-col items-center pb-4">
    <Avatar size="lg" src="/company-placeholder.png" />
    <h5 class="mb-1 text-xl font-medium text-gray-900 dark:text-white">
      {company.company_name}
    </h5>
    <span class="text-sm text-gray-500 dark:text-gray-400"
      >{company.industry}</span
    >
    <div class="flex mt-4 space-x-3 rtl:space-x-reverse lg:mt-6">
      <Button on:click={viewDetail}>View Details</Button>
      <Button on:click={viewSimilar} color="light" class="dark:text-white"
        >View similar</Button
      >
    </div>
  </div>
</Card>
