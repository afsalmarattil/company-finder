<script lang="ts">
  import {
    DarkMode,
    NavBrand,
    NavHamburger,
    Navbar,
    Search,
    ToolbarButton,
  } from "flowbite-svelte";

  import UserMenu from "../user/UserMenu.svelte";
  import {
    fetchCompanies,
    searchCompanies,
    searchQuery,
  } from "$lib/stores/companyStore";

  import { CogOutline } from "flowbite-svelte-icons";
  import { goto } from "$app/navigation";

  export let fluid = true;
  export let drawerHidden = false;
  export let list = false;

  let query = "";

  const handleSearchInput = (event: Event) => {
    const target = event.target as HTMLInputElement;
    query = target.value;
    $searchQuery = query;
  };

  $: {
    if ($searchQuery.trim() === "") {
      fetchCompanies();
    } else {
      searchCompanies($searchQuery);
    }
  }
</script>

<Navbar {fluid} class="text-black" color="default" let:NavContainer>
  <NavContainer class="mb-px mt-px px-1" {fluid}>
    <NavHamburger
      onClick={() => (drawerHidden = !drawerHidden)}
      class="m-0 me-3 md:block lg:hidden"
    />
    <NavBrand href="/" class={list ? "w-40" : "lg:w-60"}>
      <img src="/logo.png" class="me-2.5 h-6 sm:h-8" alt="Flowbite Logo" />
      <span
        class="ml-px self-center whitespace-nowrap text-xl font-semibold dark:text-white sm:text-2xl"
      >
        Company Finder
      </span>
    </NavBrand>
    <div class="hidden lg:block lg:ps-8">
      <form on:submit|preventDefault>
        <Search
          size="md"
          class="mt-1 w-96 border focus:outline-none"
          bind:value={query}
          on:input={handleSearchInput}
        />
      </form>
    </div>
    <div
      class="ms-auto flex items-center text-gray-500 dark:text-gray-400 sm:order-2"
    >
      <ToolbarButton
        on:click={() => goto("/settings")}
        size="lg"
        class="-mx-0.5 hover:text-gray-900 dark:hover:text-white"
      >
        <CogOutline size="lg" />
      </ToolbarButton>

      <DarkMode />
      <UserMenu />
    </div>
  </NavContainer>
</Navbar>
