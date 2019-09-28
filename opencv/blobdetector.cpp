+double SimpleBlobDetectorImpl::getArea(Moments & moms) const
+{
+    return moms.m00;
+}
+
+double SimpleBlobDetectorImpl::getCircularity(Moments & moms, std::vector<Point> & contour) const
+{
+    double area = moms.m00;
+    double perimeter = arcLength(contour, true);
+    return 4 * CV_PI * area / (perimeter * perimeter);
+}
+
+double SimpleBlobDetectorImpl::getInertia(Moments & moms) const
+{
+    double denominator = std::sqrt(std::pow(2 * moms.mu11, 2) + std::pow(moms.mu20 - moms.mu02, 2));
+    const double eps = 1e-2;
+    double ratio;
+    if (denominator > eps)
+    {
+        double cosmin = (moms.mu20 - moms.mu02) / denominator;
+        double sinmin = 2 * moms.mu11 / denominator;
+        double cosmax = -cosmin;
+        double sinmax = -sinmin;
+
+        double imin = 0.5 * (moms.mu20 + moms.mu02) - 0.5 * (moms.mu20 - moms.mu02) * cosmin - moms.mu11 * sinmin;
+        double imax = 0.5 * (moms.mu20 + moms.mu02) - 0.5 * (moms.mu20 - moms.mu02) * cosmax - moms.mu11 * sinmax;
+        ratio = imin / imax;
+    }
+    else
+    {
+        ratio = 1;
+    }
+    return ratio;
+}
+
+double SimpleBlobDetectorImpl::getConvexity(std::vector<Point> & contour) const
+{
+    std::vector < Point > hull;
+    convexHull(contour, hull);
+    double area = contourArea(contour);
+    double hullArea = contourArea(hull);
+    if (fabs(hullArea) < DBL_EPSILON)
+        return -1;
+    return area / hullArea;
+}
+
+double SimpleBlobDetectorImpl::getBlobRadius(std::vector<Point> & contour, Point2d & centerLocation) const
+{
+    std::vector<double> dists;
+    for (size_t pointIdx = 0; pointIdx < contour.size(); pointIdx++)
+    {
+        Point2d pt = contour[pointIdx];
+        dists.push_back(norm(centerLocation - pt));
+    }
+    std::sort(dists.begin(), dists.end());
+    return (dists[(dists.size() - 1) / 2] + dists[dists.size() / 2]) / 2.;
+}
+
+Point2d SimpleBlobDetectorImpl::getBlogLocation(Moments & moms) const
+{
+    return Point2d(moms.m10 / moms.m00, moms.m01 / moms.m00);
+}
+
