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
          @click="setCategory(category.id)"
        >
          <img :src="category.img" alt="" />
          <p>{{ category.name }}</p>
        </div>
      </div>
    </section>
    <section class="desktop">
      <h1 class="font-primary">¡OH NO, SE ME HAN OLVIDADO LAS LLAVES!</h1>
      <p>All travels</p>
    </section>
  </div>
</template>

<script>
import AutoComplete from "../components/AutoComplete";
import store from "../store/index";

export default {
  data() {
    return {
      render_categories: null,
      categories: [
        {
          id: 1,
          name: "Libros",
          img: require("@/assets/categories/libro.jpg"),
        },
        {
          id: 2,
          name: "Tuppers",
          img: require("@/assets/categories/libro.jpg"),
        },
        {
          id: 3,
          name: "Juguetes",
          img: require("@/assets/categories/libro.jpg"),
        },
        {
          id: 4,
          name: "Tecnología",
          img: require("@/assets/categories/libro.jpg"),
        },
        {
          id: 5,
          name: "Ropa",
          img: require("@/assets/categories/libro.jpg"),
        },
        {
          id: 6,
          name: "Accesorios",
          img: require("@/assets/categories/libro.jpg"),
        },
        {
          id: 7,
          name: "Electronica",
          img: require("@/assets/categories/libro.jpg"),
        },
        {
          id: 8,
          name: "Coches",
          img: require("@/assets/categories/libro.jpg"),
        },
      ],
    };
  },
  methods: {
    setCategory(id) {
      console.log("prueba");
      store.commit("SET_CATEGORY", id);
    },
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

.categories {
  display: flex;
  flex-wrap: wrap;
  padding: 20px 30px;
  justify-content: space-between;
}

.category {
  position: relative;
  margin: 5px 0px;
}

.category p {
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

.category img {
  width: calc(50vw - 40px);
  height: calc(50vw - 40px);
  border-radius: 10%;
  object-fit: cover; /* or object-fit: contain; */
}
</style>
