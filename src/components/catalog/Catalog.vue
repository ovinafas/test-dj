<template>
  
<section>
    <div class="container">
        <div class="row">
            <!-- NewProduct_items -->
            <div class="col-sm-12 padding-right">
            <!-- RetailSale_items -->
              <RetailSale></RetailSale>
            <!-- category-tab -->
            <category-tab></category-tab>
            </div>
        </div>
    </div>
</section>
</template>

<script>
// @ is an alias to /src
import CategoryTab from "./CategoryTab.vue";
import RetailSale from "./RetailSale.vue";

export default {
  name: "Catalog",
  components: {
    CategoryTab ,
    RetailSale
  }
};
</script>
