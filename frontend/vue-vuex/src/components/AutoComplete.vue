<template>
  <div>
    <InputText
      class="autocomplete"
      :placeholder="placeholder"
      v-model="search"
    />
  </div>
</template>

<script>
import InputText from "primevue/inputtext";

export default {
  name: "AutoComplete",
  props: {
    data: Array,
    placeholder: String,
  },
  emits: ["update:modelValue"],
  methods: {
    searchCategory(value) {
      if (!value) {
        this.$emit("update:modelValue", this.data);
      } else {
        let response = this.data.filter((element) => {
          return element.name.toLowerCase().startsWith(value.toLowerCase());
        });
        this.$emit("update:modelValue", response);
      }
    },
  },
  computed: {
    search: {
      get() {
        return this.search;
      },
      set(value) {
        this.searchCategory(value);
      },
    },
  },
  components: {
    InputText,
  },
};
</script>

<style scoped>
.autocomplete {
  width: 100%;
}
</style>
