<template>
  <div>
    <LocateAction />
    <ActionsForm v-if="actionFound" />
    <MissingAction v-if="actionNotFound" />
    <Actions/>
  </div>
</template>

<script>
import LocateAction from '@/components/main/LocateAction.vue'
import ActionsForm from '@/components/actionForms/ActionsForm.vue'
import MissingAction from '@/components/actionForms/MissingAction.vue'
import Actions from '@/components/main/Actions.vue'
import { mapGetters, mapActions } from "vuex";

export default {
  name: "Main",
  components: {
    LocateAction,
    ActionsForm,
    MissingAction,
    Actions,
  },
  computed: {
    ...mapGetters("data", ["actionFound", "actionNotFound",]),
  },
};
</script>

