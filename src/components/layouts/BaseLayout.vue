<template>
  <div>
        <!-- header -->
        <main-header></main-header>
        <!-- slider -->
        <slot name="slider"></slot>
        <!-- content -->
        <slot></slot>
        <!-- footer -->
        <MainFooter />
  </div>
</template>

<script>
// @ is an alias to /src
import MainHeader from "@/components/layouts/MainHeader";
import MainFooter from "@/components/layouts/MainFooter";
export default {
  name: "BaseLayout",
  components: {
    MainHeader,
    MainFooter
  }
};
</script>
