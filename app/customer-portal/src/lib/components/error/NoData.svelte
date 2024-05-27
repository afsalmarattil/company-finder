<script lang="ts">
  import { Badge } from "flowbite-svelte";
  export let message: string;
</script>

<div class="flex flex-col justify-center items-center h-full">
  <Badge class="px-10 py-4">
    <p class="text-2xl">{message}</p>
  </Badge>
</div>
