<template>
  <div class="categories_shipping">
    <section class="mobile">
      <h1 class="font-primary">¿Qué se te ha olvidado?</h1>

      <AutoComplete
        class="search-autocomplete"
        :data="data"
        v-model="filteredData"
        placeholder="Categoria"
      />

      <div class="data">
        <div
          class="element"
          v-for="element in render_data"
          :key="element.id"
          @click="onElement(element.id)"
        >
          <img :src="element.image" alt="" />
          <p>{{ element.name }}</p>
        </div>
      </div>
    </section>
    <section class="desktop">
      <div class="image-vector">
        <h1 class="font-secundary">¡OH NO, SE ME HAN OLVIDADO LAS LLAVES!</h1>
      </div>
    </section>
  </div>
</template>

<script>
import AutoComplete from "../components/AutoComplete";

export default {
  name: "CategoriesShipping",
  props: ["data"],
  emits: ["update:modelValue"],
  data() {
    return {
      render_data: null,
    };
  },
  mounted() {
    this.filteredData = [...this.data];
  },
  methods: {
    onElement(id) {
      this.$emit("update:modelValue", id);
    },
  },
  computed: {
    filteredData: {
      get() {
        return this.filteredData;
      },
      set(value) {
        this.render_data = value;
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
  padding-bottom: 70px;
}

.page .mobile .data {
  display: flex;
  flex-wrap: wrap;
  padding: 20px 30px;
  justify-content: space-between;
}

.page .mobile .element {
  position: relative;
  margin: 5px 0px;
}

.page .mobile .element p {
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

.page .mobile .element img {
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
