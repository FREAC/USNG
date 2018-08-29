import pandas


def from_list(data):

    df = None
    error = None
    try:
        if len(data) == 2:
            df = pandas.DataFrame.from_records([data])
        else:
            df = pandas.DataFrame.from_records(data)
    except AssertionError as e:
        error = e
    finally:
        return df, error


def from_csv(data):

    df = None
    error = None
    try:
        df = pandas.read_csv(data)
    except FileNotFoundError as e:
        error = e
    finally:
        return df, error


def from_shapefile(data):

    import shapefile
    xs = None
    ys = None
    error = None
    try:
        sf = shapefile.Reader(data)
        shapes = sf.shapes()
        # Only accept Point, PointZ and PointM geometries
        if sf.shapes()[0].shapeType in (1, 11, 21):
            xs = pandas.Series(shape.points[0][0] for shape in shapes)
            ys = pandas.Series(shape.points[0][1] for shape in shapes)
    except shapefile.ShapefileException as e:
        error = e
    finally:
        return xs, ys, error
