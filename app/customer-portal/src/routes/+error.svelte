<script lang="ts">
  import "../app.css";
  import { page } from "$app/stores";
  import NotFound from "$lib/pages/NotFound.svelte";
  import ServerError from "$lib/pages/ServerError.svelte";

  const pages = {
    404: NotFound,
    500: ServerError,
  };

  const status = +$page.status;
  const index = Object.keys(pages)
    .map((x) => +x)
    .reduce((p, c) => (p < status ? c : p));
  const component = pages[index];
</script>

<svelte:component this={component}></svelte:component>
