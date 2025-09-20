import { onMounted, onUnmounted } from "vue";

export function useEscapeKey(callback: () => void) {
  const handleEsc = (e: KeyboardEvent) => {
    if (e.key === "Escape" || e.key === "Esc") {
      callback();
    }
  };

  onMounted(() => {
    window.addEventListener("keydown", handleEsc);
  });

  onUnmounted(() => {
    window.removeEventListener("keydown", handleEsc);
  });
}




// import { onMounted, onUnmounted, watch, type Ref } from "vue";

// export function useEscapeKey(callback: () => void, isActive?: Ref<boolean>) {
//   const handleEsc = (e: KeyboardEvent) => {
//     if (e.key === "Escape" || e.key === "Esc") {
//       callback();
//     }
//   };

//   const addListener = () => window.addEventListener("keydown", handleEsc);
//   const removeListener = () => window.removeEventListener("keydown", handleEsc);

//   onMounted(() => {
//     if (isActive) {
//       // следим за состоянием модалки
//       watch(
//         isActive,
//         (active) => {
//           if (active) {
//             addListener();
//           } else {
//             removeListener();
//           }
//         },
//         { immediate: true }
//       );
//     } else {
//       addListener();
//     }
//   });

//   onUnmounted(() => {
//     removeListener();
//   });
// }