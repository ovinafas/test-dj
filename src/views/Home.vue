<template>
  <base-layout>
  <template v-slot:slider>
    <Slider />
  </template>
  <template v-slot:default>
    <Catalog />
  </template>
  </base-layout>
</template>

<script>
// @ is an alias to /src
import BaseLayout from "@/components/layouts/BaseLayout.vue";
import Catalog from "@/components/catalog/Catalog.vue";
import Slider from "@/components/catalog/Slider.vue";
export default {
  name: "Home",
  components: {
    BaseLayout,
    Catalog,
    Slider
  }
};
</script>
