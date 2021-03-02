<template>
  <div class="page prueba">
    <CategoriesShipping
      v-if="state.shipping.category == null"
      :data="categories"
      v-model="idcatgeory"
    />
    <FiltersShipping
      v-if="state.shipping.category != null && state.shipping.filters == null"
      v-model="filters"
    />
    <TravelsShipping
      v-if="
        state.shipping.category != null &&
          state.shipping.filters != null &&
          state.shipping.travel == null
      "
      :data="travels"
      v-model="idtravel"
    />
  </div>
</template>

<script>
// Components
import CategoriesShipping from "../components/CategoriesShipping";
import FiltersShipping from "../components/FiltersShipping";
import TravelsShipping from "../components/TravelsShipping";

// Vue
import { mapActions } from "vuex";
import { computed, onMounted, ref } from "vue";
import { useStore } from "vuex";

// Api
import { categoryApi } from "../api";

export default {
  setup() {
    const store = useStore();
    const state = computed(() => store.state);
    let categories = ref([]);

    onMounted(async () => {
      let response = await categoryApi.getCategories();
      categories.value = response.data.categories;
    });

    return {
      state,
      categories,
    };
  },
  data() {
    return {
      idcatgeory: "",
      filters: {},
      idtravel: "",
      travels: [
        {
          id: 1,
          name: "Juan Esparza",
          stars: 5,
          start_time: "13:00h",
          origin_location: "Ontinyent, Valencia",
          destination_location: "Alcoy, Valencia",
          price: 6.2,
          img: "https://thispersondoesnotexist.com/image",
        },
        {
          id: 2,
          name: "Xema Garcia",
          stars: 3,
          start_time: "16:00h",
          origin_location: "Ontinyent, Valencia",
          price: 7.2,
          destination_location: "Muro de Alcoy, Valencia",
          img: "https://thispersondoesnotexist.com/image",
        },
        {
          id: 3,
          name: "Pedro Iglesias",
          stars: 4,
          start_time: "11:00h",
          origin_location: "Ontinyent, Valencia",
          destination_location: "Alicante, Valencia",
          price: 5.2,
          img: "https://thispersondoesnotexist.com/image",
        },
        {
          id: 4,
          name: "Tono Canario",
          stars: 2,
          start_time: "22:00h",
          price: 3.2,
          origin_location: "Alcoy, Valencia",
          destination_location: "Ontinyent, Valencia",
          img: "https://thispersondoesnotexist.com/image",
        },
      ],
    };
  },
  methods: {
    ...mapActions({
      setCategory: "shipping/setCategory",
      seFilters: "shipping/seFilters",
    }),
  },
  watch: {
    idcatgeory: function(val) {
      this.setCategory(val);
    },
    filters: function(val) {
      this.seFilters(val);
    },
  },
  components: {
    CategoriesShipping,
    FiltersShipping,
    TravelsShipping,
  },
};
</script>

<style>
.search-autocomplete {
  margin: 0px 30px;
  width: calc(100% - 60px);
}
</style>

<style scoped>
.page .mobile {
  flex-direction: column;
  padding-bottom: 70px;
}

.page .mobile .categories {
  display: flex;
  flex-wrap: wrap;
  padding: 20px 30px;
  justify-content: space-between;
}

.page .mobile .category {
  position: relative;
  margin: 5px 0px;
}

.page .mobile .category p {
  position: absolute;
  top: 0;
  font-weight: bold;
  color: white;
  font-size: 7vw;
  height: 100%;
  margin: 0;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.page .mobile .category img {
  width: calc(50vw - 40px);
  height: calc(50vw - 40px);
  border-radius: 10%;
  object-fit: cover; /* or object-fit: contain; */
  filter: brightness(70%);
}

.page .desktop {
  flex-direction: column;
  padding-bottom: 70px;
}

.page .desktop .image-vector {
  background-image: url("../assets/fondo_home_sustituto.png");
  height: 400px;
  width: 100vw;
  background-size: cover;
  background-position-y: center;
}
</style>
