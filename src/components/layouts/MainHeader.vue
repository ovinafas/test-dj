<template>
  <div>
        <!-- header -->
       <h2>{{title}}</h2>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "MainHeader",
  components: {
    // HelloWorld
  },
  data: function() {
      return {
          title: 'Main Header'
      }
      
  }
};
</script>
