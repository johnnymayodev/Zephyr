<script>
  import ThemeSwitcher from "./components/themeswitcher.svelte";
  import Button from "./components/button.svelte";
</script>

<ThemeSwitcher />

<main class="w-fit max-md:w-3/5 mx-auto my-32 text-base">
  <article class="prose my-8">
    <h4 class="text-xl font-medium">Thank you for checking out</h4>
    <h1 class="text-8xl max-md:text-6xl font-bold">Zephyr</h1>

    <p>
      Zephyr is a lightweight and easy to use component-based front-end
      framework. It is built with Python and leverages Svelte for its files.
    </p>
    <p>
      Zephyr uses Python to compile the page then runs an HTTP server to serve
      the page. Tailwind CSS and daisyUI are built into Zephyr. This allows for
      rapid development and easy customization.
    </p>
    <p>
      Zephyr is made for developers who want to learn the fundamentals of
      component-based frameworks and be able to practice using a mainstream CSS
      and UI framework.
    </p>
  </article>

  <Button />
</main>
