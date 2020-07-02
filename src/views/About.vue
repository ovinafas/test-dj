<template>
  <base-layout>
  <template v-slot:default>
    <div class="about">
    <h1>This is an about page</h1>
  </div>
  </template>
  </base-layout>
</template>

<script>
// @ is an alias to /src
import BaseLayout from "@/components/layouts/BaseLayout.vue";
export default {
  name: "About",
  components: {
    BaseLayout
  }
};
</script>
