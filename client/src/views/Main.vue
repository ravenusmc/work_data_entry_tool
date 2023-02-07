<template>
  <div>
    TST-TST-2023-0001
    Missing Actions: TST-TST-2023-0002
    <LocateAction />
    <ActionsForm v-if="actionFound" />
    <MissingAction v-if="actionNotFound" />
  </div>
</template>

<script>
import LocateAction from '@/components/main/LocateAction.vue'
import ActionsForm from '@/components/actionForms/ActionsForm.vue'
import MissingAction from '@/components/actionForms/MissingAction.vue'
import { mapGetters, mapActions } from "vuex";

export default {
  name: "Main",
  components: {
    LocateAction,
    ActionsForm,
    MissingAction,
  },
  computed: {
    ...mapGetters("data", ["actionFound", "actionNotFound",]),
  },
  // data() {
  //   return {
  //     actionNumber: "",
  //   };
  // },
  // methods: {
  //   ...mapActions("data", ["locateAction"]),
  //   findAction(evt) {
  //     evt.preventDefault();
  //     const payload = {
  //       actionNumber: this.actionNumber,
  //     };
  //     this.locateAction({ payload });
  //   },
  // },
};
</script>

