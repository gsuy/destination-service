from function import model, scaleup , findNearGrid ,convert_data_to_model

def predictModel(tripInfo):
    data_scaledown = convert_data_to_model(tripInfo)
    if type(data_scaledown) == bool:
        return "invalid day!"
    result = model.predict(data_scaledown)[0].tolist()
    result = scaleup(result)
    grid_near = findNearGrid(result)
    return {"latitude":result[1] ,"longtitude":result[0] ,"grid_near_name": grid_near}
    