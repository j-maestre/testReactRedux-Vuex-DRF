<template>
  <div class="page">
    <section class="mobile">
      <div class="profile-image">
        <img src="https://thispersondoesnotexist.com/image" alt="profile" />
      </div>
      <div class="info">
        <div class="follows">
          <span>25</span>
          <p>Envios</p>
        </div>
        <div class="travels">
          <span>42</span>
          <p>Viajes</p>
        </div>
      </div>
      <hr />
      <div class="panel-control">
        <router-link
          active-class="active"
          v-for="route in routes"
          :key="route.label"
          :to="route.to"
          class="option"
        >
          <i :class="route.icon"></i>
          <p>{{ route.label }}</p>
        </router-link>
        <div @click="logout()" class="option" to="/profile">
          <i class="fas fa-sign-out-alt"></i>
          <p>Cerrar Session</p>
        </div>
      </div>
    </section>

    <section class="desktop">
      <article class="menu">
        <div class="img">
          <img src="https://thispersondoesnotexist.com/image" alt="profile" />
        </div>
        <div class="info">
          <div class="follows">
            <span>25</span>
            <p>Envios</p>
          </div>
          <div class="travels">
            <span>42</span>
            <p>Viajes</p>
          </div>
        </div>
        <hr />
        <div class="options">
          <router-link
            active-class="active"
            v-for="route in routes"
            :key="route.label"
            :to="route.to"
            class="option"
          >
            <i :class="route.icon"></i>
            <p>{{ route.label }}</p>
          </router-link>
          <div @click="logout()" class="option" to="/profile">
            <i class="fas fa-sign-out-alt"></i>
            <p>Cerrar Session</p>
          </div>
        </div>
      </article>
      <article class="content">
        <router-view />
      </article>
    </section>
  </div>
</template>

<script>
import { useStore } from "vuex";
import { useRouter } from "vue-router";

export default {
  components: {},
  setup() {
    const store = useStore();
    const router = useRouter();

    const logout = () => {
      store.dispatch("user/logout");
      router.push({ name: "Home" });
    };

    let routes = [
      { label: "Editar perfil", icon: "fas fa-user-edit", to: "/profile/edit" },
      { label: "Mis viajes", icon: "fas fa-route", to: "/profile/travels" },
      { label: "Mis envios", icon: "fas fa-box", to: "/profile/shippings" },
      { label: "Ajustes", icon: "fas fa-cog", to: "/profile/settings" },
    ];

    return { logout, routes };
  },
};
// <Password v-model="value" />
</script>

<style scoped>
.mobile {
  flex-direction: column;
  padding-bottom: 70px;
}

.mobile .profile-image {
  width: 100vw;
  height: 200px;
  position: relative;
  background-color: black;
  margin-bottom: 20px;
}

.mobile .profile-image img {
  width: 160px;
  height: 160px;
  object-fit: cover;
  position: absolute;
  left: calc(50vw - 80px);
  bottom: -40px;
  border-radius: 100%;
}

.mobile .panel-control {
  width: 100%;
  display: flex;
  font-size: 20px;
  flex-direction: column;
}

.mobile .panel-control i {
  font-size: 25px;
}

.mobile .panel-control .option {
  font-size: 18px;
  border: 1px solid black;
  width: calc(100% - 40px);
  padding: 15px 20px;
  margin: 10px 20px;
  display: flex;
}

.mobile .panel-control .option p {
  margin: 0px 15px;
}

.mobile .info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-weight: bold;
  padding: 0px 30px;
}

.mobile .info div {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin-right: 10px;
}

.mobile hr {
  margin: 20px 30px;
  height: 3px;
  background-color: black;
  border: none;
  box-shadow: none;
}
.mobile .info span {
  font-size: 28px;
}

.mobile .info p {
  font-size: 17px;
  margin: 0px;
}

.desktop {
  display: flex;
  background: rgb(230, 230, 230);
  height: calc(100% - 100px);
}

.desktop article {
  min-height: 700px;
  background: white;
  margin: 50px 2vw;
  overflow: hidden;
}

.desktop .menu {
  width: 22vw;
  padding: 30px;
  position: relative;
  padding-top: 310px;
}

.desktop .menu .img {
  height: 200px;
  width: 100%;
  background-color: black;
  position: absolute;
  top: 0;
  left: 0;
}

.desktop .menu .img img {
  width: 130px;
  border-radius: 100%;
  object-fit: cover;
  position: absolute;
  left: calc(50% - 65px);
  bottom: -30px;
}

.desktop .menu .option {
  display: flex;
  padding: 15px;
  margin: 10px;
}

.desktop .menu .option.active,
.desktop .menu .option:hover {
  background-color: #faff8a;
}

.desktop .menu .option p {
  margin: 0px 10px;
}

.desktop .info {
  display: flex;
  text-align: center;
  font-weight: bold;
  position: absolute;
  justify-content: space-around;
  top: 230px;
  left: 0;
  width: 100%;
}

.desktop .info div {
  margin-right: 20px;
}

.desktop .info span {
  font-size: 30px;
}

.desktop .info p {
  margin: 0;
}
.desktop .content {
  width: 70vw;
}

.desktop hr {
  height: 3px;
  margin-bottom: 20px;
  background-color: black;
  border: none;
  box-shadow: none;
}
</style>
