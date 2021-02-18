<template>
  <div class="travels">
    <div class="mobile">
      <h3 class="font-secundary">Aqui estan los viajes disponibles!</h3>
      <div
        v-if="!filters"
        class="button-primary button"
        @click="filters = true"
      >
        <p>VER FILTROS</p>
      </div>
      <div v-if="filters" class="filters">
        <h3 class="font-tertiary">Fecha del viaje:</h3>
        <div class="input-false">
          {{ shipping.filters.date }}
        </div>
        <h3 class="font-tertiary">De:</h3>
        <div class="input-false">
          {{ shipping.filters.location_origin }}
        </div>
        <h3 class="font-tertiary">A:</h3>
        <div class="input-false">
          {{ shipping.filters.location_destination }}
        </div>
      </div>
      <div class="filters-hide">
        <hr />
        <div @click="filters = false" class="hidden">
          <i v-if="filters" class="fas fa-chevron-up"></i>
        </div>
      </div>

      <div class="travels">
        <div class="travel" v-for="travel in data" :key="travel.id">
          <h3>{{ travel.name }}</h3>
          <strong>{{ travel.start_time }}</strong>
          <Rating
            :modelValue="travel.stars"
            :readonly="true"
            :stars="5"
            class="rating"
            :cancel="false"
          />
          <img :src="travel.img" alt="" />
          <p class="price">{{ travel.price }}€</p>
          <p class="location">
            {{ travel.origin_location }} - {{ travel.destination_location }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// Compoenents
import Rating from "primevue/rating";

// Vue
import { computed } from "vue";
import { useStore } from "vuex";

export default {
  name: "TravelsShipping",
  props: ["data"],
  emits: ["update:modelValue"],
  data() {
    return {
      filters: false,
    };
  },
  setup() {
    const store = useStore();
    const shipping = computed(() => store.state.shipping);

    return { shipping };
  },
  mounted() {},
  methods: {},
  computed: {},
  components: {
    Rating,
  },
};
</script>
<style scoped>
.mobile {
  flex-direction: column;
  padding-bottom: 70px;
}

.mobile .input-false {
  color: #495057;
  border: 1px solid #ced4da;
  border-radius: 3px;
  margin: 0px 30px;
  width: calc(100% - 60px);
  padding: 15px;
  background: rgb(238, 238, 238);
  display: flex;
  align-items: center;
  justify-content: center;
}

.mobile .filters-hide hr {
  background-color: black;
  border: none;
  height: 2px;
  width: calc(100% - 60px);
  margin: 20px 30px;
  position: absolute;
}

.mobile .filters-hide .hidden {
  position: relative;
  font-size: 30px;
  left: calc(50% - 20px);
  top: 18px;
  width: 40px;
  height: 40px;
  border-bottom-left-radius: 20%;
  border-bottom-right-radius: 20%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.mobile .button {
  width: calc(100% - 60px);
  margin: 0px 30px;
  text-align: center;
  border: 2px solid black;
}

.mobile .button p {
  margin: 0;
}

.mobile .travels {
  width: 100%;
  padding: 0px 30px;
}

.mobile .travels .travel {
  border: 2px solid black;
  height: 140px;
  padding: 10px 20px;
  margin: 15px 0px;
  background-color: #ffffff;
  display: grid;
  grid-template-columns: 35% 33% 33%;
  grid-template-areas:
    "image name name"
    "image location location"
    "rating time price";
}

.mobile .travels .travel img {
  width: 80px;
  grid-area: image;
  justify-self: left;
  align-self: center;
}

.mobile .travels .travel h3 {
  grid-area: name;
  margin: 0;
}

.mobile .travels .travel strong {
  grid-area: time;
  align-self: center;
  justify-self: left;
}

.mobile .travels .travel .rating {
  grid-area: rating;
  align-self: center;
  justify-self: left;
}

.mobile .travels .travel p.price {
  grid-area: price;
  margin: 0;
  font-weight: bold;
  font-size: 25px;
  align-self: center;
  justify-self: right;
}

.mobile .travels .travel p.location {
  grid-area: location;
  margin: 0;
}
</style>

<style>
span.p-rating-icon.pi.pi-star,
span.p-rating-icon.pi.pi-star-o {
  font-size: 12px;
  margin: 1px;
}
</style>
