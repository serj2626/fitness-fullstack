<script setup>
import {
  YandexMap,
  YandexMapControls,
  YandexMapDefaultFeaturesLayer,
  YandexMapDefaultSchemeLayer,
  YandexMapZoomControl,
  YandexMapMarker,
} from "vue-yandex-maps";
const map = shallowRef(null);

defineProps({
  mobHeight: {
    type: String,
    default: "500px",
  },
  tabHeight: {
    type: String,
    default: "500px",
  },
  lapHeight: {
    type: String,
    default: "600px",
  },
  deskHeight: {
    type: String,
    default: "600px",
  },
  mapWidth: {
    type: String,
    default: "59.844032",
  },
  mapLongitude: {
    type: String,
    default: "30.392647",
  },
});
</script>

<template>
  <section v-if="mapLongitude && mapWidth" class="base-map">
    <ClientOnly>
      <YandexMap
        v-model="map"
        :settings="{
          coordorder: 'latlong',
          location: {
            center: [parseFloat(mapLongitude), parseFloat(mapWidth)],
            zoom: 15,
          },
          showScaleInCopyrights: true,
          behaviors: ['drag', 'dblClick'],
          theme: 'dark',
          className: 'base-map__map',
          // camera: {tilt: 45 * (Math.PI / 180), azimuth: 30 * (Math.PI / 180)}
        }"
        width="100%"
        height="100%"
      >
        <YandexMapDefaultSchemeLayer />
        <YandexMapDefaultFeaturesLayer>
          <yandex-map-controls :settings="{ position: 'right' }">
            <yandex-map-zoom-control />
          </yandex-map-controls>
          <YandexMapMarker
            :settings="{
              coordinates: [parseFloat(mapLongitude), parseFloat(mapWidth)],
            }"
            position="translate(-36%, -72%)"
          >
            <div class="base-map__map-marker">
              <Icon name="icon:marker" class="base-map__map-marker-icon" />
              <div class="base-map__map-marker-effect" />
            </div>
          </YandexMapMarker>
        </YandexMapDefaultFeaturesLayer>
      </YandexMap>
    </ClientOnly>
  </section>
</template>

<style lang="scss" scoped>
.__ymap_container {
  height: 100%;
  background-color: #292626;
}

.base-map {
  position: relative;
  width: 100%;
  height: v-bind(mobHeight);
  background-color: black; // Устанавливаем черный фон для карты

  @include mediaTablet {
    height: v-bind(tabHeight);
  }

  @include mediaLaptop {
    height: v-bind(lapHeight);
  }

  @include mediaDesktop {
    height: v-bind(deskHeight);
  }

  &__map {
    border-radius: 0 !important;
    overflow: hidden;

    &-marker {
      width: 50px;
      height: 50px;
      color: red;
      font-size: 54px;
      position: relative;
      &-effect {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: #f25757;
        border-radius: 50%;
        opacity: 0.4;
        transform: scale(0);
        animation: pulse 2s ease-out infinite;
        z-index: -1;
      }
    }
  }
}

.base-map__map {
  border-radius: 0 !important; // Убираем скругления
  overflow: hidden;
}

@keyframes pulse {
  0% {
    transform: scale(
      0.8
    ); /* Начинаем не с 0.5, а с 0.8 — меньше резкого скачка */
    opacity: 0.4;
  }
  50% {
    opacity: 0.6; /* Плавное увеличение прозрачности в середине анимации */
  }
  100% {
    transform: scale(1.8); /* Уменьшаем конечный масштаб (было 2) */
    opacity: 0; /* Плавное затухание */
  }
}
</style>
