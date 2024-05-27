<script lang="ts">
  export let icon;
  export let title: string;
  export let value: string;
</script>

<div class="flex items-center space-x-2">
  <svelte:component this={icon} class="text-gray-500 h-5 w-5" />
  <div class="flex-1 min-w-0">
    <p class="text-sm font-medium text-gray-500 truncate dark:text-gray-400">
      {title}
    </p>
    <p class="text-md capitalize font-medium text-gray-900 dark:text-white">
      {value}
    </p>
  </div>
</div>
