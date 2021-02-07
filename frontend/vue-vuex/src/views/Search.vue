<template>
  <div class="page">
    <section class="mobile">
      <h1 class="font-primary">¿Qué se te ha olvidado?</h1>

      <AutoComplete
        class="search-autocomplete"
        :data="categories"
        v-model="filteredCategories"
        placeholder="Categoria"
      />

      <div class="categories">
        <div
          class="category"
          v-for="category in render_categories"
          :key="category.id"
        >
          <img :src="category.img" alt="" />
          {{ category.name }}
        </div>
      </div>
      {{ filteredCategories }}
    </section>
    <section class="desktop">
      <h1 class="font-primary">¡OH NO, SE ME HAN OLVIDADO LAS LLAVES!</h1>
    </section>
  </div>
</template>

<script>
import AutoComplete from "../components/AutoComplete";

export default {
  data() {
    return {
      render_categories: null,
      categories: [
        {
          id: 1,
          name: "Libros",
          img: require("@/assets/categories/libro.png"),
        },
        {
          id: 2,
          name: "Tuppers",
          img: "img.jpg",
        },
        {
          id: 3,
          name: "Juguetes",
          img: "img.jpg",
        },
        {
          id: 4,
          name: "Tgecnología",
          img: "img.jpg",
        },
        {
          id: 5,
          name: "Ropa",
          img: "img.jpg",
        },
        {
          id: 6,
          name: "Accesorios",
          img: "img.jpg",
        },
      ],
    };
  },
  mounted() {
    this.filteredCategories = [...this.categories];
  },
  computed: {
    filteredCategories: {
      get() {
        return this.filteredCategories;
      },
      set(value) {
        this.render_categories = value;
      },
    },
  },
  components: {
    AutoComplete,
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
}
.category {
  width: 100px;
  height: 100px;
}
</style>
