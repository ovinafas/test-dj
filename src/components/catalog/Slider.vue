<template>
  <section id="slider">
    <!--slider-->
    <div class="container">
      <div class="row">
        <div class="col-sm-12">
          <div id="slider-carousel" class="carousel slide" data-ride="carousel">
            <ol class="carousel-indicators">
              <li
                data-target="#slider-carousel"
                data-slide-to="0"
                class="active"
              ></li>
              <li data-target="#slider-carousel" data-slide-to="1"></li>
            </ol>

            <div class="carousel-inner">
                <SliderItem></SliderItem>
            </div>

            <a
              href="#slider-carousel"
              class="left control-carousel hidden-xs"
              data-slide="prev"
            >
              <i class="fa fa-angle-left"></i>
            </a>
            <a
              href="#slider-carousel"
              class="right control-carousel hidden-xs"
              data-slide="next"
            >
              <i class="fa fa-angle-right"></i>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!--/slider-->
</template>

<script>
import SliderItem from "./SliderItem";
export default {
  name: `Slider`,
  props: {
    // products: [],
    // category: null,
  },
  components: {
    SliderItem,
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
