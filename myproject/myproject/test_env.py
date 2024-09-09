# import os

# # Get the environment variable
# connection_string = os.getenv('APPLICATIONINSIGHTS_CONNECTION_STRING')

# # Print the environment variable
# print(f'APPLICATIONINSIGHTS_CONNECTION_STRING={connection_string}')







@login_required
def api(request):
    form = ApiForm()  # Initialize form variable

    with tracer.start_as_current_span("api_span"):
        url_api = os.getenv('URL_API')
        client_id = os.getenv('CLIENT_ID')
        client_secret = os.getenv('CLIENT_SECRET')

        if not url_api or not client_id or not client_secret:
            logger.error("Missing environment variables.")
            return render(request, 'myapp/formulaire.html', {'form': form, 'error': 'Configuration error'})

        if request.method == 'POST':
            form = ApiForm(request.POST)
            if form.is_valid():
                with tracer.start_as_current_span("form_processing"):
                    image_url = form.cleaned_data['image_url']
                    # Log the received image URL
                    logger.info(f"Image URL received: {image_url}")

                    # API Request
                    auth = (client_id, client_secret)
                    params = {'url': image_url}
                    with tracer.start_as_current_span("external_api_request"):
                        try:
                            response = requests.get(url_api, params=params, auth=auth)
                            response.raise_for_status()
                            prediction_data = response.json().get('faces', [])
                            # Log the prediction result
                            logger.info(f"Prediction Data: {prediction_data}")

                            # Save prediction data to the database
                            prediction_instance = ImagePrediction.objects.create(image_url=image_url, prediction_data=prediction_data)
                            # Convert timestamp to local time
                            local_time = timezone.localtime(prediction_instance.timestamp)
                            # Record prediction metrics
                            prediction_counter_per_minute.add(1)

                            return render(
                                request,
                                'myapp/reponse_formulaire.html',
                                {'form': form, 'info': prediction_data, 'nombre_personne': len(prediction_data), 'url': image_url, 'timestamp': local_time}
                            )
                        except requests.RequestException as e:
                            logger.error(f"API request failed: {e}")
                            result = {'error': 'API request failed'}
            else:
                result = {'form': form}

        return render(request, 'myapp/formulaire.html', {'form': form, **result})