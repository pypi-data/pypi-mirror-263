import pkg_resources

# Replace 'package_name' with the name of the package you're interested in
dist = pkg_resources.get_distribution('caluxPy-fi')

# Access the PKG-INFO file
metadata = dist.get_metadata(dist.PKG_INFO)
print(metadata)