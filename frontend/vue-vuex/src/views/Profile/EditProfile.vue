<template>
  <div class="page">
    <section class="desktop">
      <h1 class="font-tertiary">Actualiza tu perfil!</h1>
      <div class="group">
        <div class="subgroup">
          <label>Nombre</label>
          <InputText type="text" v-model="form.name" />
          <label>Apellidos</label>
          <InputText type="text" v-model="form.surnames" />
          <label>Email</label>
          <InputText type="text" v-model="form.email" disabled />
          <label>Telefono de contacto</label>
          <InputText type="text" v-model="form.tel" />
        </div>
        <div class="subgroup image">
          <label>Imagen de perfil</label>
          <img src="https://thispersondoesnotexist.com/image" alt="profile" />
          <FileUpload
            mode="basic"
            name="demo[]"
            url="./upload.php"
            accept="image/*"
            :maxFileSize="1000000"
            @upload="onUpload"
          />
        </div>
      </div>
      <div class="group">
        <div class="subgroup2">
          <label>Biografia</label>
          <Textarea v-model="form.bio" rows="7" />
        </div>
      </div>
      <div class="button-primary button">
        Guardar cambios
      </div>
    </section>
  </div>
</template>

<script>
import Textarea from "primevue/textarea";
import FileUpload from "primevue/fileupload";
import InputText from "primevue/inputtext";
import { reactive } from "vue";
import { useStore } from "vuex";

export default {
  components: { Textarea, FileUpload, InputText },
  setup() {
    const store = useStore();
    let response = store.dispatch("user/getProfile");
    let form = reactive({
      name: "",
      surnames: "",
      email: "",
      tel: "",
      bio: "",
    });

    response.then((data) => {
      console.log(data);
      form.name = data.data.user.name;
      form.surnames = data.data.user.surnames;
      form.email = data.data.user.email;
      form.tel = data.data.user.tel;
      form.bio = data.data.user.bio;
    });

    let updateProfile = store.dispatch("user/updateProfile");

    return { form, updateProfile };
  },
};
</script>

<style scoped>
.page {
  padding: 30px;
}

.desktop {
  flex-direction: column;
}

.page .desktop .group {
  display: flex;
}

.page .desktop .group label {
  margin: 15px 0px;
  font-weight: bold;
  font-size: 17px;
}

.page .desktop .subgroup {
  width: 50%;
  display: flex;
  flex-direction: column;
}

.page .desktop .subgroup.image {
  justify-content: center;
  align-items: center;
}

.page .desktop .subgroup2 {
  width: 100%;
  display: flex;
  flex-direction: column;
}

.page .desktop .subgroup img {
  width: 60%;
  margin-bottom: 20px;
}

.page .desktop .subgroup .button {
}
</style>
