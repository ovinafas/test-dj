<template>
  <div class="item row active">
    <div class="col-sm-6">
      <h1><span>SHOP</span>CENTER</h1>
      <h2>Shop Center</h2>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua.
      </p>
      <button type="button" class="btn btn-default get">
        Get it now
      </button>
    </div>
    <div class="col-sm-6">
      <img
        src="/static/images/home/girl2.jpg"
        class="girl img-responsive"
        alt=""
      />
      <img src="/static/images/home/pricing.png" class="pricing" alt="" />
    </div>
  </div>
  <!--/slider-->
</template>

<script>
// import SingleProduct from "./SingleProduct";
export default {
  name: `SliderItem`,
  props: {
    // products: [],
    // category: null,
  },
  components: {
    // SingleProduct,
  },
  data() {
    return {
      //   page: 1,
      //   perPage: 4,
      //   pages: []
    };
  },
  //   methods: {

  //   },
  //   watch: {

  //   },
  //   computed: {

  //   },
};
</script>
