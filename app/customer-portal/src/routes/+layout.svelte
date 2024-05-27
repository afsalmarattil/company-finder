<script>
  import "../app.css";
  import Footer from "$lib/components/footer/Footer.svelte";
  import NavBar from "$lib/components/navbar/NavBar.svelte";
  import { Toaster } from "svelte-french-toast";
</script>

<main>
  <div class="flex flex-col min-h-screen bg-gray-100 dark:bg-gray-900">
    <header
      class="fixed top-0 z-40 w-full border-b border-gray-200 bg-white dark:border-gray-600 dark:bg-gray-800"
    >
      <NavBar />
    </header>

    <div class="flex-1 pt-[80px] p-10">
      <slot />
    </div>

    <div class="px-10">
      <Footer />
    </div>
  </div>
  <Toaster />
</main>
