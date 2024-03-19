/*
 * This file is part of the CoverageControl library
 *
 * Author: Saurav Agarwal
 * Contact: sauravag@seas.upenn.edu, agr.saurav1@gmail.com
 * Repository: https://github.com/KumarRobotics/CoverageControl
 *
 * Copyright (c) 2024, Saurav Agarwal
 *
 * The CoverageControl library is free software: you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or (at your
 * option) any later version.
 *
 * The CoverageControl library is distributed in the hope that it will be
 * useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
 * Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along with
 * CoverageControl library. If not, see <https://www.gnu.org/licenses/>.
 */

/*!
 * \file polygon_utils.h
 * \brief Provides utilities for polygon manipulation using CGAL.
 */

#ifndef CPPSRC_CORE_INCLUDE_COVERAGECONTROL_CGAL_POLYGON_UTILS_H_
#define CPPSRC_CORE_INCLUDE_COVERAGECONTROL_CGAL_POLYGON_UTILS_H_

#include <vector>

#include "CoverageControl/typedefs.h"

namespace CoverageControl {

/*! \brief Partition a polygon into y-monotone polygons
 *
 * @param[in] polygon The input polygon
 * @param[out] y_monotone_polygons The output y-monotone polygons
 */
void PolygonYMonotonePartition(PointVector const &polygon,
                               std::vector<PointVector> &y_monotone_polygons);

} /* namespace CoverageControl */

#endif  // CPPSRC_CORE_INCLUDE_COVERAGECONTROL_CGAL_POLYGON_UTILS_H_
