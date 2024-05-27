<script lang="ts">
  import type { Company } from "$lib/types/company";
  import { Card, Avatar, Button } from "flowbite-svelte";
  import { goto } from "$app/navigation";

  export let company: Company;

  function viewDetail() {
    goto(`/companies/${company.id}`);
  }
</script>

<div
  class="w-full px-4 py-5 bg-white dark:bg-gray-800 text-gray-900 dark:text-white shadow-sm rounded-lg hover:shadow-lg"
>
  <div class="flex items-center space-x-4 rtl:space-x-reverse">
    <Avatar
      src="/company-placeholder.png"
      alt="comany-logo"
      class="flex-shrink-0"
    />
    <div class="flex-1 min-w-0">
      <p class="text-sm font-medium text-gray-900 truncate dark:text-white">
        {company.company_name}
      </p>
      <p class="text-sm text-gray-500 truncate dark:text-gray-400">
        {company.industry}
      </p>
    </div>
    <Button size="xs" color="light" on:click={viewDetail}>view</Button>
  </div>
</div>
