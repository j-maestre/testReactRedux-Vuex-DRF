<template>
  <div class="filters_shipping">
    <section class="mobile">
      <div class="location">
        <h3 class="font-primary">¿Que dia te vendria bien?</h3>
        <datepicker v-model="picked" class="form-input" />
      </div>
      <div class="location">
        <h3 class="font-primary">¿Donde está tu objeto?</h3>
        <InputText
          class="form-input"
          type="text"
          placeholder="Ubicacion Origen"
          v-model="filters.location_origin"
        />
        <!-- <vue-google-autocomplete
          id="location-origin"
          classname="form-control"
          class="form-input"
          placeholder="Ubicacion"
          v-on:placechanged="getLocationOrigin()"
        >
        </vue-google-autocomplete> -->
      </div>
      <div class="location">
        <h3 class="font-primary">¿Donde estás tu?</h3>
        <InputText
          class="form-input"
          placeholder="Ubicacion Destino"
          type="text"
          v-model="filters.location_destination"
        />
        <!-- <vue-google-autocomplete
          id="location-destination"
          class="form-input"
          classname="form-control"
          placeholder="Ubicacion"
          v-on:placechanged="getLocationDestination()"
        >
        </vue-google-autocomplete> -->
      </div>
      <!-- <img src="../assets/maps.png" alt="" /> -->
      <div class="next-button">
        <div class="button-primary button" @click="next()">
          <p>Siguiente</p>
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
// import VueGoogleAutocomplete from "vue-google-autocomplete";
import Datepicker from "vue3-datepicker";
import { ref } from "vue";
import InputText from "primevue/inputtext";

export default {
  name: "FiltersShipping",
  emits: ["update:modelValue"],
  setup() {
    const picked = ref(new Date());

    navigator.geolocation.getCurrentPosition(
      getCoordinates,
      errorGetCoordinates
    );

    function getCoordinates(position) {
      //Closure para establecer las coordenadas actuales del usuario
      let coords = {
        latitude: position.coords.latitude,
        longitude: position.coords.longitude,
      };
      console.log(position);
      console.log(coords);
    }

    function errorGetCoordinates(error) {
      alert("ALERTA! No se han podido obtener las coordenadas");
      console.log(error);
    }

    return {
      picked,
    };
  },
  data() {
    return {
      filters: {
        location_origin: "",
        location_destination: "",
        date: "",
      },
    };
  },
  methods: {
    getLocationOrigin(addressData) {
      this.filters.location_origin = addressData;
    },
    getLocationDestination(addressData) {
      this.filters.location_destination = addressData;
    },
    next() {
      let dateObj = new Date(this.picked);
      var month = dateObj.getUTCMonth() + 1; //months from 1-12
      var day = dateObj.getUTCDate();
      var year = dateObj.getUTCFullYear();
      let newdate = year + "/" + month + "/" + day;

      this.filters.date = newdate;
      this.$emit("update:modelValue", this.filters);
    },
  },
  components: {
    // VueGoogleAutocomplete,
    Datepicker,
    InputText,
  },
};
</script>

<style scoped>
.filters_shipping {
  height: calc(100vh - 165px);
}

.filters_shipping .mobile {
  flex-direction: column;
  justify-content: space-between;
  padding-bottom: 70px;
}

.filters_shipping .mobile img {
  margin-top: 30px;
  height: 300px;
  position: absolute;
  bottom: 60px;
}

.next-button {
  background-color: white;
  width: 100%;
  margin-top: 20px;
}

.filters_shipping .mobile .next-button .button {
  cursor: pointer;
  margin: 10px 30px;
  text-align: center;
  border: 2px solid black;
}

.filters_shipping .mobile .next-button .button p {
  margin: 0;
}
</style>

<style>
.filters_shipping .mobile .form-input {
  color: #495057;
  border: 1px solid #ced4da;
  border-radius: 3px;
  margin: 0px 30px;
  width: calc(100% - 60px);
  padding: 15px;
  background-color: white;
  font-size: 16px;
}
.v3dp__popout {
  margin: 0px 30px;
  width: calc(100% - 60px) !important;
}
</style>
