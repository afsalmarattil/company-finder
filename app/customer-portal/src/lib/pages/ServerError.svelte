<script lang="ts">
  import { Button, P } from "flowbite-svelte";
  import { ArrowLeftOutline } from "flowbite-svelte-icons";
  export let title = "Something has gone seriously wrong";
  export let description =
    "It's always time for a coffee break. We should be back by the time you finish your coffee.";
  export let image = {
    src: "/500.png",
    alt: "error",
  };
  export let btnHref = "/";
  export let btnTitle = "Go back home";

  export let mainDivClass =
    "flex flex-col justify-center items-center px-6 mx-auto h-screen xl:px-0 dark:bg-gray-900";
  export let h1Class =
    "mb-3 text-2xl font-bold leading-tight text-gray-900 sm:text-4xl lg:text-5xl dark:text-white";
  export let imgDiv = "block md:max-w-lg";
  export let div2Class = "text-center xl:max-w-4xl";
</script>

<div class={mainDivClass}>
  <div class={imgDiv}>
    <img src={image.src} alt={image.alt} />
  </div>
  <div class={div2Class}>
    <h1 class={h1Class}>
      {title}
    </h1>
    <P
      class="mb-5 text-base font-normal text-gray-500 dark:text-gray-400 md:text-lg"
    >
      {description}
    </P>
    <Button href={btnHref}>
      <ArrowLeftOutline />
      {btnTitle}
    </Button>
  </div>
</div>
