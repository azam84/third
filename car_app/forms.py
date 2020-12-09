from django import forms

from car_app.models import car_filtering_logs, car_information, car_information_details, MarkaModel, ModelYear, YearEngine, EngineGearbox, GearboxTransmission, TransmissionBantype, BantypeFueltype


class car_filtering_logsCreationForm(forms.ModelForm):
    class Meta:
        model = car_filtering_logs
        fields = ['marka', 'model', 'year', 'engine']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['model'].queryset = MarkaModel.objects.all()
        self.fields['year'].queryset = ModelYear.objects.all()
        self.fields['engine'].queryset = YearEngine.objects.all()
        # self.fields['gearbox'].queryset = EngineGearbox.objects.none()
        #self.fields['transmission'].queryset = GearboxTransmission.objects.none()
        #self.fields['ban_type'].queryset = TransmissionBantype.objects.none()
        #self.fields['fuel_type'].queryset = BantypeFueltype.objects.none()

        # if 'marka' in self.data:
        #     try:
        #         marka_id = int(self.data.get('marka'))
        #         self.fields['model'].queryset = MarkaModel.objects.filter(marka=marka_id)
        #         #print(self.fields['model'].queryset)
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty Model queryset

        # if 'model' in self.data:
        #     try:
        #         model_id = int(self.data.get('model'))
        #         self.fields['year'].queryset = ModelYear.objects.filter(model=model_id).order_by('year')
        #         print("form year")
        #         print(self.fields['year'].queryset)
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty year queryset
        

        # if 'year' in self.data:
        #     try:
        #         year_id = int(self.data.get('year'))
        #         self.fields['engine'].queryset = YearEngine.objects.filter(marka=marka_id, model=model_id, year=year_id)
        #         print("form engine")
        #         print(self.fields['engine'].queryset)
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty engine queryset

        # if 'engine' in self.data:
        #     try:
        #         engine_id = int(self.data.get('engine'))
        #         self.fields['gearbox'].queryset = EngineGearbox.objects.filter(engine=engine_id)
        #         #print(self.fields['gearbox'].queryset)
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty gearbox queryset

        # if 'gearbox' in self.data:
        #     try:
        #         gearbox_id = int(self.data.get('gearbox'))
        #         self.fields['transmission'].queryset = GearboxTransmission.objects.filter(gearbox=gearbox_id)
        #         #print(self.fields['transmission'].queryset)
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty transmission queryset


        # if 'transmission' in self.data:
        #     try:
        #         transmission_id = int(self.data.get('transmission'))
        #         self.fields['ban_type'].queryset = TransmissionBantype.objects.filter(transmission=transmission_id)
        #         #print(self.fields['ban_type'].queryset)
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty bantype queryset


        # if 'bantype' in self.data:
        #     try:
        #         bantype_id = int(self.data.get('ban_type'))
        #         self.fields['fuel_type'].queryset = BantypeFueltype.objects.filter(bantype=bantype_id)
        #         #print(self.fields['fuel_type'].queryset)
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty fueltype queryset
    

# class car_information_detailsCreationForm(forms.ModelForm):
#     class Meta:
#         model = car_information_details
#         fields = ['alloy_wheels', 'luke', 'leather_salon', 'start_stop', 'monitor','front_bumper', 'front_hood', 'front_right_corner', 'front_left_corner', 'front_right_door', 'front_left_door', 'dam', 'back_left_door', 'back_right_door', 'back_right_corner', 'back_left_corner', 'begaj', 'back_bumper', 'right_pole', 'left_pole', 'color']
#
#
#         def __init__(self, *args, **kwargs):
#             self._cid = kwargs.pop('m_id.id', None)
#             print("((((((((((((((((((((((((((((((((((((((")
#             print(self._cid)
#             super().__init__(*args, **kwargs)