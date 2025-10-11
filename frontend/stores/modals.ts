export type ModalItem =
  | "menu"
  | "reviewListCoach"
  | "reviewCoachForm"
  | "success"
  | "feedback"
  | "auth"
  | "order"
  | "orderAbonement"
  | "orderTraining"
  | "service";

export const useModalsStore = defineStore("modals-store", () => {
  const activeModals = ref<Map<ModalItem, Record<string, unknown>>>(new Map());

  function checkKey(event: KeyboardEvent) {
    if (event.key === "Escape") {
      closeAllModals();
    }
  }

  const getModalData = (modal: ModalItem) => {
    return activeModals.value.get(modal);
  };

  const openModal = (modal: ModalItem, props?: any) => {
    if (document) {
      document.documentElement.style.overflowY = "hidden";
      document.body.style.paddingRight = "6px";
      document.body.style.marginRight = "7px";
      document.addEventListener("keydown", checkKey, { once: true });
    }
    activeModals.value.set(modal, props);
  };

  const closeModal = (modal: ModalItem) => {
    activeModals.value.delete(modal);
    if (!activeModals.value.size && document) {
      document.documentElement.style.overflowY = "auto";
      document.body.style.paddingRight = "0";
      document.body.style.marginRight = "0";
    }
  };

  const closeAllModals = () => {
    const headerCatalogMenu = document.getElementById("header-catalog-menu");

    if (menuIsOpen) {
      headerCatalogMenu?.classList.add("header-catalog-menu_close");
      activeModals.value.clear();
      document && (document.documentElement.style.overflowY = "auto");
    }
  };

  const isAnyModalOpen = computed(
    () => activeModals.value && !!activeModals.value.size
  );

  const menuIsOpen = computed(() => activeModals.value.has("register"));

  return {
    activeModals,
    openModal,
    closeModal,
    closeAllModals,
    isAnyModalOpen,
    menuIsOpen,
    getModalData,
  };
});
