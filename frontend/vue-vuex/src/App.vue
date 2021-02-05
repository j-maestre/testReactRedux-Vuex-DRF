<template>
  <div id="app">
    <Header></Header>
    <router-view />
    <!-- 
    <p>Count: {{ count }}</p>
    <button @click="increment()">Increment</button>
    <button @click="decrement()">Decrement</button> -->
  </div>
</template>

<script>
import Header from "./components/Header";

import { computed } from "vue";
import { useStore } from "vuex";
export default {
  name: "App",
  setup() {
    const store = useStore();
    const count = computed(() => store.state.count);

    function increment() {
      store.commit("increment");
    }
    function decrement() {
      store.commit("decrement");
    }
    return { count, increment, decrement };
  },
  components: {
    Header,
  },
};
</script>
