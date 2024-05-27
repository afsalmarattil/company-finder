<script>
  import { Breadcrumb, BreadcrumbItem, Dropzone } from "flowbite-svelte";
  import { UploadOutline, UploadSolid } from "flowbite-svelte-icons";
  import { uploadCSV } from "$lib/stores/companyStore";

  import toast from "svelte-french-toast";

  const handleChange = async (event) => {
    const selectedFiles = event.target?.files;
    if (selectedFiles.length > 0) {
      toast.promise(uploadCSV(selectedFiles[0]), {
        loading: "Uploading CSV...",
        success: "CSV successfully uploaded!",
        error: "Failed to upload CSV.",
      });
    }
  };
</script>

<svelte:head>
  <title>Settings | Company Finder</title>
</svelte:head>

<div class="flex p-4 justify-between align-middle">
  <h1 class="text-xl dark:text-white">Settings</h1>
  <Breadcrumb aria-label="Default breadcrumb example">
    <BreadcrumbItem href="/companies" home>Companies</BreadcrumbItem>
    <BreadcrumbItem href="/settings">Settings</BreadcrumbItem>
  </Breadcrumb>
</div>

<Dropzone id="dropzone" on:change={handleChange}>
  <UploadSolid class="w-8 h-8 text-gray-700 dark:text-gray-200" />
  <p class="mt-4 mb-4 text-sm text-gray-500 dark:text-gray-400">
    <span class="font-semibold">Click to upload</span> or drag and drop
  </p>
  <p class="text-xs text-gray-500 dark:text-gray-400">csv file</p>
</Dropzone>
