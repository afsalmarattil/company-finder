<script lang="ts">
  import {
    Avatar,
    Dropdown,
    DropdownHeader,
    DropdownItem,
  } from "flowbite-svelte";

  export let name: string = "Guest";
  export let email: string = "";
</script>

<button class="ms-3 rounded-full ring-gray-400 focus:ring-4 dark:ring-gray-600">
  <Avatar size="sm" border />
</button>
<Dropdown placement="bottom-end">
  <DropdownHeader>
    <span class="block text-sm">{name}</span>
    <span class="block truncate text-sm font-medium">{email}</span>
  </DropdownHeader>
  <DropdownItem>Sign out</DropdownItem>
</Dropdown>
